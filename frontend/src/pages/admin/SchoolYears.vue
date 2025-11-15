<script lang="ts">
export const description = "School Years management page"
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

import { Plus, MoreHorizontal } from "lucide-vue-next"

const userRole = "Admin"

// Dummy School Years data
const schoolYears = ref([
  {
    id: 1,
    year: "2024-2025",
    status: "Active",
    color: "bg-green-500",
  },
  {
    id: 2,
    year: "2023-2024",
    status: "Completed",
    color: "bg-blue-500",
  },
  {
    id: 3,
    year: "2022-2023",
    status: "Completed",
    color: "bg-yellow-500",
  },
  {
    id: 4,
    year: "2021-2022",
    status: "Completed",
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
      <header
        class="flex h-16 shrink-0 items-center gap-2 px-4 transition-all"
      >
        <SidebarTrigger class="-ml-2" />
        <Separator orientation="vertical" class="mx-2 h-4" />

        <Breadcrumb>
          <BreadcrumbList>
            <BreadcrumbItem>
              <BreadcrumbLink href="/admin/dashboard">Admin</BreadcrumbLink>
            </BreadcrumbItem>
            <BreadcrumbSeparator />
            <BreadcrumbItem>
              <BreadcrumbPage>School Years</BreadcrumbPage>
            </BreadcrumbItem>
          </BreadcrumbList>
        </Breadcrumb>
      </header>

      <!-- Content -->
      <div class="flex flex-1 flex-col gap-4 p-4 pt-0">
        <!-- Top Bar -->
        <div class="flex items-center justify-between">
          <div>
            <h2 class="text-2xl font-bold tracking-tight">School Years</h2>
            <p class="text-sm text-muted-foreground">
              Manage academic school years and statuses.
            </p>
          </div>

          <Button class="flex items-center gap-2">
            <Plus class="h-4 w-4" />
            Add School Year
          </Button>
        </div>

        <Card>
          <CardHeader>
            <CardTitle>School Years Overview</CardTitle>
            <CardDescription>
              View, edit, or close school years.
            </CardDescription>
          </CardHeader>

          <CardContent>
            <!-- Search -->
            <div class="flex items-center justify-between mb-4">
              <Input
                v-model="search"
                placeholder="Search school years..."
                class="max-w-xs"
              />
            </div>

            <!-- Table -->
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead class="w-56">School Year</TableHead>
                  <TableHead>Status</TableHead>
                  <TableHead class="text-right w-20">Actions</TableHead>
                </TableRow>
              </TableHeader>

              <TableBody>
                <TableRow
                  v-for="sy in schoolYears"
                  :key="sy.id"
                  class="hover:bg-muted/50"
                >
                  <!-- School Year -->
                  <TableCell>
                    <div class="flex items-center gap-2">
                      <div
                        class="h-3 w-3 rounded-full"
                        :class="sy.color"
                      ></div>
                      <p class="font-medium">{{ sy.year }}</p>
                    </div>
                  </TableCell>

                  <!-- Status -->
                  <TableCell>
                    <Badge
                      :variant="sy.status === 'Active' ? 'default' : 'secondary'"
                    >
                      {{ sy.status }}
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

                        <DropdownMenuItem>Edit</DropdownMenuItem>
                        <DropdownMenuItem>Mark as Completed</DropdownMenuItem>

                        <DropdownMenuSeparator />

                        <DropdownMenuItem class="text-red-600">
                          Delete School Year
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
