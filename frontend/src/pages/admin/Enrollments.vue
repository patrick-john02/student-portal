<script lang="ts">
export const description = "Enrollments management page"
export const iframeHeight = "800px"
export const containerClass = "w-full h-full"
</script>

<script setup lang="ts">
import { ref } from "vue"

import AppSidebar from "@/components/sidebars/AppSidebar.vue"
import {
  SidebarProvider,
  SidebarInset,
  SidebarTrigger,
} from "@/components/ui/sidebar"

import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbList,
  BreadcrumbLink,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/components/ui/breadcrumb"

import { Separator } from "@/components/ui/separator"

import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
} from "@/components/ui/card"

import { Button } from "@/components/ui/button"
import { Badge } from "@/components/ui/badge"
import { Input } from "@/components/ui/input"

import {
  Table,
  TableHeader,
  TableRow,
  TableHead,
  TableBody,
  TableCell,
} from "@/components/ui/table"

import {
  DropdownMenu,
  DropdownMenuTrigger,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
} from "@/components/ui/dropdown-menu"

import { Plus, MoreHorizontal, User, Layers } from "lucide-vue-next"

const userRole = "Admin"

// Dummy enrollment data
const enrollments = ref([
  {
    id: 1,
    student: "John Mark Rivera",
    lrn: "123456789012",
    grade: "Grade 11",
    section: "STEM A",
    status: "Enrolled",
    color: "bg-green-500",
  },
  {
    id: 2,
    student: "Andrea Lopez",
    lrn: "987654321098",
    grade: "Grade 11",
    section: "HUMSS B",
    status: "Pending",
    color: "bg-yellow-500",
  },
  {
    id: 3,
    student: "Rico Delos Santos",
    lrn: "456789123456",
    grade: "Grade 12",
    section: "ABM A",
    status: "Enrolled",
    color: "bg-blue-500",
  },
  {
    id: 4,
    student: "Kyla Francisco",
    lrn: "654321987654",
    grade: "Grade 12",
    section: "GAS C",
    status: "Dropped",
    color: "bg-red-500",
  },
])

const search = ref("")
</script>

<template>
  <SidebarProvider>
    <AppSidebar :userRole="userRole" />

    <SidebarInset>
      <!-- Header -->
      <header class="flex h-16 shrink-0 items-center gap-2 px-4 transition-all">
        <SidebarTrigger class="-ml-2" />
        <Separator orientation="vertical" class="mx-2 h-4" />

        <Breadcrumb>
          <BreadcrumbList>
            <BreadcrumbItem>
              <BreadcrumbLink href="/admin/dashboard">Admin</BreadcrumbLink>
            </BreadcrumbItem>
            <BreadcrumbSeparator />
            <BreadcrumbItem>
              <BreadcrumbPage>Enrollments</BreadcrumbPage>
            </BreadcrumbItem>
          </BreadcrumbList>
        </Breadcrumb>
      </header>

      <!-- Content -->
      <div class="flex flex-1 flex-col gap-4 p-4 pt-0">

        <!-- Top Bar -->
        <div class="flex items-center justify-between">
          <div>
            <h2 class="text-2xl font-bold tracking-tight">Enrollments</h2>
            <p class="text-sm text-muted-foreground">
              Manage student enrollments per grade and section.
            </p>
          </div>

          <Button class="flex items-center gap-2">
            <Plus class="h-4 w-4" />
            Add Enrollment
          </Button>
        </div>

        <Card>
          <CardHeader>
            <CardTitle>Enrollments Overview</CardTitle>
            <CardDescription>
              View, add, or update student enrollment records.
            </CardDescription>
          </CardHeader>

          <CardContent>
            <!-- Search -->
            <div class="flex items-center justify-between mb-4">
              <Input
                v-model="search"
                placeholder="Search students..."
                class="max-w-xs"
              />
            </div>

            <!-- Table -->
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead class="w-64">Student</TableHead>
                  <TableHead>LRN</TableHead>
                  <TableHead>Grade Level</TableHead>
                  <TableHead>Section</TableHead>
                  <TableHead>Status</TableHead>
                  <TableHead class="text-right w-20">Actions</TableHead>
                </TableRow>
              </TableHeader>

              <TableBody>
                <TableRow
                  v-for="en in enrollments"
                  :key="en.id"
                  class="hover:bg-muted/50"
                >
                  <!-- Student -->
                  <TableCell>
                    <div class="flex items-center gap-2">
                      <User class="h-4 w-4 text-muted-foreground" />
                      <span class="font-medium">{{ en.student }}</span>
                    </div>
                  </TableCell>

                  <!-- LRN -->
                  <TableCell class="text-muted-foreground">
                    {{ en.lrn }}
                  </TableCell>

                  <!-- Grade -->
                  <TableCell class="text-muted-foreground">
                    {{ en.grade }}
                  </TableCell>

                  <!-- Section -->
                  <TableCell class="flex items-center gap-2">
                    <Layers class="h-4 w-4 text-muted-foreground" />
                    <span>{{ en.section }}</span>
                  </TableCell>

                  <!-- Status -->
                  <TableCell>
                    <Badge
                      :variant="
                        en.status === 'Enrolled'
                          ? 'default'
                          : en.status === 'Pending'
                          ? 'secondary'
                          : 'destructive'
                      "
                    >
                      {{ en.status }}
                    </Badge>
                  </TableCell>

                  <!-- Actions -->
                  <TableCell class="text-right">
                    <DropdownMenu>
                      <DropdownMenuTrigger as-child>
                        <Button variant="ghost" size="icon">
                          <MoreHorizontal class="h-4 w-4" />
                        </Button>
                      </DropdownMenuTrigger>

                      <DropdownMenuContent align="end">
                        <DropdownMenuLabel>Actions</DropdownMenuLabel>
                        <DropdownMenuSeparator />

                        <DropdownMenuItem>View Details</DropdownMenuItem>
                        <DropdownMenuItem>Edit Enrollment</DropdownMenuItem>

                        <DropdownMenuSeparator />

                        <DropdownMenuItem class="text-red-600">
                          Remove Enrollment
                        </DropdownMenuItem>
                      </DropdownMenuContent>
                    </DropdownMenu>
                  </TableCell>
                </TableRow>
              </TableBody>
            </Table>
          </CardContent>
        </Card>
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>
